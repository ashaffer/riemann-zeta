import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk14 :
    P2RoundedFactorCheckpointData.panel16Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix56_eq :
    P2RoundedFactorCheckpointData.panel16Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk14.1

theorem panel16Prefix57_eq :
    P2RoundedFactorCheckpointData.panel16Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk14.2.1

theorem panel16Prefix58_eq :
    P2RoundedFactorCheckpointData.panel16Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk14.2.2.1

theorem panel16Prefix59_eq :
    P2RoundedFactorCheckpointData.panel16Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk14.2.2.2

end RHP2Bridge

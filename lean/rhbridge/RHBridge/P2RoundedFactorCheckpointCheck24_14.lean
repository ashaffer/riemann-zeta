import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk14 :
    P2RoundedFactorCheckpointData.panel24Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix56_eq :
    P2RoundedFactorCheckpointData.panel24Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk14.1

theorem panel24Prefix57_eq :
    P2RoundedFactorCheckpointData.panel24Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk14.2.1

theorem panel24Prefix58_eq :
    P2RoundedFactorCheckpointData.panel24Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk14.2.2.1

theorem panel24Prefix59_eq :
    P2RoundedFactorCheckpointData.panel24Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk14.2.2.2

end RHP2Bridge

import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk5 :
    P2RoundedFactorCheckpointData.panel16Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix20_eq :
    P2RoundedFactorCheckpointData.panel16Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk5.1

theorem panel16Prefix21_eq :
    P2RoundedFactorCheckpointData.panel16Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk5.2.1

theorem panel16Prefix22_eq :
    P2RoundedFactorCheckpointData.panel16Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk5.2.2.1

theorem panel16Prefix23_eq :
    P2RoundedFactorCheckpointData.panel16Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk5.2.2.2

end RHP2Bridge

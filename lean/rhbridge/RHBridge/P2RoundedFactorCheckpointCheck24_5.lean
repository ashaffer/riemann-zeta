import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk5 :
    P2RoundedFactorCheckpointData.panel24Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix20_eq :
    P2RoundedFactorCheckpointData.panel24Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk5.1

theorem panel24Prefix21_eq :
    P2RoundedFactorCheckpointData.panel24Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk5.2.1

theorem panel24Prefix22_eq :
    P2RoundedFactorCheckpointData.panel24Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk5.2.2.1

theorem panel24Prefix23_eq :
    P2RoundedFactorCheckpointData.panel24Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk5.2.2.2

end RHP2Bridge

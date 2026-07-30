import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk9 :
    P2RoundedFactorCheckpointData.panel23Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix36_eq :
    P2RoundedFactorCheckpointData.panel23Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk9.1

theorem panel23Prefix37_eq :
    P2RoundedFactorCheckpointData.panel23Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk9.2.1

theorem panel23Prefix38_eq :
    P2RoundedFactorCheckpointData.panel23Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk9.2.2.1

theorem panel23Prefix39_eq :
    P2RoundedFactorCheckpointData.panel23Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk9.2.2.2

end RHP2Bridge

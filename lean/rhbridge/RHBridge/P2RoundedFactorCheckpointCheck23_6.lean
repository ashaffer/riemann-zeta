import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk6 :
    P2RoundedFactorCheckpointData.panel23Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix24_eq :
    P2RoundedFactorCheckpointData.panel23Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk6.1

theorem panel23Prefix25_eq :
    P2RoundedFactorCheckpointData.panel23Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk6.2.1

theorem panel23Prefix26_eq :
    P2RoundedFactorCheckpointData.panel23Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk6.2.2.1

theorem panel23Prefix27_eq :
    P2RoundedFactorCheckpointData.panel23Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk6.2.2.2

end RHP2Bridge

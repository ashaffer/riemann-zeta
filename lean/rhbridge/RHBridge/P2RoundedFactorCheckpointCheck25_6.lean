import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk6 :
    P2RoundedFactorCheckpointData.panel25Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix24_eq :
    P2RoundedFactorCheckpointData.panel25Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk6.1

theorem panel25Prefix25_eq :
    P2RoundedFactorCheckpointData.panel25Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk6.2.1

theorem panel25Prefix26_eq :
    P2RoundedFactorCheckpointData.panel25Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk6.2.2.1

theorem panel25Prefix27_eq :
    P2RoundedFactorCheckpointData.panel25Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk6.2.2.2

end RHP2Bridge

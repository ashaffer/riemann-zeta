import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk6 :
    P2RoundedFactorCheckpointData.panel7Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix24_eq :
    P2RoundedFactorCheckpointData.panel7Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk6.1

theorem panel7Prefix25_eq :
    P2RoundedFactorCheckpointData.panel7Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk6.2.1

theorem panel7Prefix26_eq :
    P2RoundedFactorCheckpointData.panel7Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk6.2.2.1

theorem panel7Prefix27_eq :
    P2RoundedFactorCheckpointData.panel7Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk6.2.2.2

end RHP2Bridge

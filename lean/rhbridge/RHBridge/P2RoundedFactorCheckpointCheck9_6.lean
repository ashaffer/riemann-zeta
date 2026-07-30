import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk6 :
    P2RoundedFactorCheckpointData.panel9Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix24_eq :
    P2RoundedFactorCheckpointData.panel9Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk6.1

theorem panel9Prefix25_eq :
    P2RoundedFactorCheckpointData.panel9Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk6.2.1

theorem panel9Prefix26_eq :
    P2RoundedFactorCheckpointData.panel9Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk6.2.2.1

theorem panel9Prefix27_eq :
    P2RoundedFactorCheckpointData.panel9Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk6.2.2.2

end RHP2Bridge

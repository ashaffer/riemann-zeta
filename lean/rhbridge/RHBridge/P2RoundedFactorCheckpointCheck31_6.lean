import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk6 :
    P2RoundedFactorCheckpointData.panel31Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix24_eq :
    P2RoundedFactorCheckpointData.panel31Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk6.1

theorem panel31Prefix25_eq :
    P2RoundedFactorCheckpointData.panel31Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk6.2.1

theorem panel31Prefix26_eq :
    P2RoundedFactorCheckpointData.panel31Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk6.2.2.1

theorem panel31Prefix27_eq :
    P2RoundedFactorCheckpointData.panel31Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk6.2.2.2

end RHP2Bridge

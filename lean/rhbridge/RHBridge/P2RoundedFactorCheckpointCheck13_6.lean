import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk6 :
    P2RoundedFactorCheckpointData.panel13Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix24_eq :
    P2RoundedFactorCheckpointData.panel13Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk6.1

theorem panel13Prefix25_eq :
    P2RoundedFactorCheckpointData.panel13Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk6.2.1

theorem panel13Prefix26_eq :
    P2RoundedFactorCheckpointData.panel13Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk6.2.2.1

theorem panel13Prefix27_eq :
    P2RoundedFactorCheckpointData.panel13Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk6.2.2.2

end RHP2Bridge

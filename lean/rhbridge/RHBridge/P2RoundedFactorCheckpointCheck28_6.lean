import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk6 :
    P2RoundedFactorCheckpointData.panel28Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix24_eq :
    P2RoundedFactorCheckpointData.panel28Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk6.1

theorem panel28Prefix25_eq :
    P2RoundedFactorCheckpointData.panel28Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk6.2.1

theorem panel28Prefix26_eq :
    P2RoundedFactorCheckpointData.panel28Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk6.2.2.1

theorem panel28Prefix27_eq :
    P2RoundedFactorCheckpointData.panel28Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk6.2.2.2

end RHP2Bridge

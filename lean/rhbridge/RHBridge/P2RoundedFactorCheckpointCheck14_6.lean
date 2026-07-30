import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk6 :
    P2RoundedFactorCheckpointData.panel14Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix24_eq :
    P2RoundedFactorCheckpointData.panel14Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk6.1

theorem panel14Prefix25_eq :
    P2RoundedFactorCheckpointData.panel14Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk6.2.1

theorem panel14Prefix26_eq :
    P2RoundedFactorCheckpointData.panel14Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk6.2.2.1

theorem panel14Prefix27_eq :
    P2RoundedFactorCheckpointData.panel14Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk6.2.2.2

end RHP2Bridge

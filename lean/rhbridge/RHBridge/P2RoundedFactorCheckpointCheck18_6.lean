import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk6 :
    P2RoundedFactorCheckpointData.panel18Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix24_eq :
    P2RoundedFactorCheckpointData.panel18Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk6.1

theorem panel18Prefix25_eq :
    P2RoundedFactorCheckpointData.panel18Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk6.2.1

theorem panel18Prefix26_eq :
    P2RoundedFactorCheckpointData.panel18Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk6.2.2.1

theorem panel18Prefix27_eq :
    P2RoundedFactorCheckpointData.panel18Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk6.2.2.2

end RHP2Bridge

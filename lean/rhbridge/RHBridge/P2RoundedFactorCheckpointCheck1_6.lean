import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk6 :
    P2RoundedFactorCheckpointData.panel1Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix24_eq :
    P2RoundedFactorCheckpointData.panel1Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk6.1

theorem panel1Prefix25_eq :
    P2RoundedFactorCheckpointData.panel1Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk6.2.1

theorem panel1Prefix26_eq :
    P2RoundedFactorCheckpointData.panel1Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk6.2.2.1

theorem panel1Prefix27_eq :
    P2RoundedFactorCheckpointData.panel1Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk6.2.2.2

end RHP2Bridge

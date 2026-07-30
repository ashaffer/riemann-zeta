import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk1 :
    P2RoundedFactorCheckpointData.panel1Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix4_eq :
    P2RoundedFactorCheckpointData.panel1Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk1.1

theorem panel1Prefix5_eq :
    P2RoundedFactorCheckpointData.panel1Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk1.2.1

theorem panel1Prefix6_eq :
    P2RoundedFactorCheckpointData.panel1Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk1.2.2.1

theorem panel1Prefix7_eq :
    P2RoundedFactorCheckpointData.panel1Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk1.2.2.2

end RHP2Bridge

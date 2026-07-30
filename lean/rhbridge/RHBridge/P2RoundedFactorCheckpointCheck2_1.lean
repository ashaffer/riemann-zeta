import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk1 :
    P2RoundedFactorCheckpointData.panel2Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix4_eq :
    P2RoundedFactorCheckpointData.panel2Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk1.1

theorem panel2Prefix5_eq :
    P2RoundedFactorCheckpointData.panel2Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk1.2.1

theorem panel2Prefix6_eq :
    P2RoundedFactorCheckpointData.panel2Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk1.2.2.1

theorem panel2Prefix7_eq :
    P2RoundedFactorCheckpointData.panel2Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk1.2.2.2

end RHP2Bridge

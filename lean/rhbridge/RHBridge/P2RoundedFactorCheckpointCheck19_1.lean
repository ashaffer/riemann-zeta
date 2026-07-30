import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk1 :
    P2RoundedFactorCheckpointData.panel19Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix4_eq :
    P2RoundedFactorCheckpointData.panel19Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk1.1

theorem panel19Prefix5_eq :
    P2RoundedFactorCheckpointData.panel19Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk1.2.1

theorem panel19Prefix6_eq :
    P2RoundedFactorCheckpointData.panel19Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk1.2.2.1

theorem panel19Prefix7_eq :
    P2RoundedFactorCheckpointData.panel19Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk1.2.2.2

end RHP2Bridge

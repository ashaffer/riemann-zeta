import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk4 :
    P2RoundedFactorCheckpointData.panel19Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix16_eq :
    P2RoundedFactorCheckpointData.panel19Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk4.1

theorem panel19Prefix17_eq :
    P2RoundedFactorCheckpointData.panel19Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk4.2.1

theorem panel19Prefix18_eq :
    P2RoundedFactorCheckpointData.panel19Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk4.2.2.1

theorem panel19Prefix19_eq :
    P2RoundedFactorCheckpointData.panel19Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk4.2.2.2

end RHP2Bridge

import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk4 :
    P2RoundedFactorCheckpointData.panel2Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix16_eq :
    P2RoundedFactorCheckpointData.panel2Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk4.1

theorem panel2Prefix17_eq :
    P2RoundedFactorCheckpointData.panel2Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk4.2.1

theorem panel2Prefix18_eq :
    P2RoundedFactorCheckpointData.panel2Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk4.2.2.1

theorem panel2Prefix19_eq :
    P2RoundedFactorCheckpointData.panel2Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk4.2.2.2

end RHP2Bridge

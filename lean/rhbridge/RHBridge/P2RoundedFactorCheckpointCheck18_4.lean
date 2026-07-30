import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk4 :
    P2RoundedFactorCheckpointData.panel18Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix16_eq :
    P2RoundedFactorCheckpointData.panel18Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk4.1

theorem panel18Prefix17_eq :
    P2RoundedFactorCheckpointData.panel18Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk4.2.1

theorem panel18Prefix18_eq :
    P2RoundedFactorCheckpointData.panel18Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk4.2.2.1

theorem panel18Prefix19_eq :
    P2RoundedFactorCheckpointData.panel18Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk4.2.2.2

end RHP2Bridge

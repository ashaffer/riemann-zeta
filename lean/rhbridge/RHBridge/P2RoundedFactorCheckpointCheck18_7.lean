import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk7 :
    P2RoundedFactorCheckpointData.panel18Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix28_eq :
    P2RoundedFactorCheckpointData.panel18Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk7.1

theorem panel18Prefix29_eq :
    P2RoundedFactorCheckpointData.panel18Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk7.2.1

theorem panel18Prefix30_eq :
    P2RoundedFactorCheckpointData.panel18Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk7.2.2.1

theorem panel18Prefix31_eq :
    P2RoundedFactorCheckpointData.panel18Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk7.2.2.2

end RHP2Bridge

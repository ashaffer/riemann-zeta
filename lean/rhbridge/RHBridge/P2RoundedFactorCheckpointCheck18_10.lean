import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk10 :
    P2RoundedFactorCheckpointData.panel18Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix40_eq :
    P2RoundedFactorCheckpointData.panel18Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk10.1

theorem panel18Prefix41_eq :
    P2RoundedFactorCheckpointData.panel18Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk10.2.1

theorem panel18Prefix42_eq :
    P2RoundedFactorCheckpointData.panel18Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk10.2.2.1

theorem panel18Prefix43_eq :
    P2RoundedFactorCheckpointData.panel18Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk10.2.2.2

end RHP2Bridge

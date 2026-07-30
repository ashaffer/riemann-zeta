import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk13 :
    P2RoundedFactorCheckpointData.panel18Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix52_eq :
    P2RoundedFactorCheckpointData.panel18Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk13.1

theorem panel18Prefix53_eq :
    P2RoundedFactorCheckpointData.panel18Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk13.2.1

theorem panel18Prefix54_eq :
    P2RoundedFactorCheckpointData.panel18Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk13.2.2.1

theorem panel18Prefix55_eq :
    P2RoundedFactorCheckpointData.panel18Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk13.2.2.2

end RHP2Bridge

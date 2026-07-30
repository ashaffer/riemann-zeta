import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk13 :
    P2RoundedFactorCheckpointData.panel1Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix52_eq :
    P2RoundedFactorCheckpointData.panel1Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk13.1

theorem panel1Prefix53_eq :
    P2RoundedFactorCheckpointData.panel1Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk13.2.1

theorem panel1Prefix54_eq :
    P2RoundedFactorCheckpointData.panel1Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk13.2.2.1

theorem panel1Prefix55_eq :
    P2RoundedFactorCheckpointData.panel1Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk13.2.2.2

end RHP2Bridge
